from database.database import Base, engine, SessionLocal
from database.models import Reading
import json
import re

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Открываем сессию
db = SessionLocal()

# Загружаем JSON
with open("database/result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Проходим по всем сообщениям
for msg in data["messages"]:

    text = msg.get("text", "")
    date = msg.get("date", "")

    # Проверяем, есть ли уже запись с таким id
    existing = db.get(Reading, msg["id"])
    if existing:
        continue

    # Температура
    temp_match = re.search(r"🌡\s*([0-9.]+)", text)
    temperature = float(temp_match.group(1)) if temp_match else None

    # ---------- ATRIUM ----------
    if "Atrium" in text:

        brightness_match = re.search(r"💡\s*(.*?)\s*🔉", text)
        noise_match = re.search(r"🔉\s*(.*)", text)

        reading = Reading(
            id=msg["id"],
            place="Atrium",
            temperature=temperature,
            brightness=brightness_match.group(1).strip() if brightness_match else None,
            noise=noise_match.group(1).strip() if noise_match else None,
            measured_at=date
        )

    # ---------- OUTSIDE ----------
    elif "Outside" in text:

        reading = Reading(
            id=msg["id"],
            place="Outside",
            temperature=temperature,
            brightness=None,
            noise=None,
            measured_at=date
        )

    # Если сообщение не подходит — пропускаем
    else:
        continue

    # Добавляем запись
    db.add(reading)

# Сохраняем изменения
db.commit()

# Закрываем соединение
db.close()

print("Импорт завершён!")