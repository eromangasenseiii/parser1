import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

print("🚀 Начинаем сбор вакансий с Habr Career...")
print("=" * 50)

def get_habr_vacancies():
    """Собирает вакансии с Habr Career"""
    all_vacancies = []
    url = "https://career.habr.com/vacancies?page=1&q=python"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"❌ Ошибка загрузки: {response.status_code}")
            return pd.DataFrame()
            
        soup = BeautifulSoup(response.content, 'html.parser')
        vacancies = soup.find_all('div', class_='vacancy-card')
        
        print(f"📄 Найдено вакансий: {len(vacancies)}")
        
        for item in vacancies[:20]:
            try:
                title_elem = item.find('a', class_='vacancy-card__title-link')
                title = title_elem.text.strip() if title_elem else "Не указано"
                
                company_elem = item.find('div', class_='vacancy-card__company-title')
                company = company_elem.text.strip() if company_elem else "Не указана"
                
                salary_elem = item.find('div', class_='basic-salary')
                salary = salary_elem.text.strip() if salary_elem else "Не указана"
                
                link = "https://career.habr.com" + title_elem['href'] if title_elem else ""
                
                all_vacancies.append({
                    'Дата сбора': datetime.now().strftime('%d.%m.%Y %H:%M'),
                    'Название': title,
                    'Компания': company,
                    'Зарплата': salary,
                    'Ссылка': link
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"❌ Ошибка: {str(e)}")
        
    return pd.DataFrame(all_vacancies)

df = get_habr_vacancies()

if len(df) == 0:
    print("❌ Не найдено вакансий. Попробуйте позже.")
    exit()

filename = f"vacancies_habr_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
df.to_excel(filename, index=False)
print("=" * 50)
print(f"✅ ГОТОВО! Собрано {len(df)} вакансий")
print(f"📁 Файл: {filename}")
print(df[['Название', 'Компания', 'Зарплата']].to_string(index=False))
