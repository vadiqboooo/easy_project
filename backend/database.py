from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс для моделей
Base = declarative_base()

# Определяем модель для таблицы Users
class User(Base):
    __tablename__ = 'users'

    tg_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String, nullable=True)  # Может быть None, если у пользователя нет username
    name = Column(String, nullable=False)
    
# Пример создания асинхронного движка и сессии
async def init_db():
    # Создаем асинхронный движок с aiosqlite
    engine = create_async_engine("sqlite+aiosqlite:///users.db", echo=True)
    
    # Создаем таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Создаем фабрику асинхронных сессий
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    
    return async_session

