# === Этап 1: Установка зависимостей с кэшированием ===
FROM node:22-alpine AS deps
WORKDIR /app

COPY package.json package-lock.json* ./
#RUN npm ci #--omit=dev  # без этого сборка моего проекта шла очень долго
RUN npm ci

# === Этап 2: Сборка приложения ===
FROM node:22-alpine AS builder

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN npm run build

# === Этап 3: Запуск сервера ===

FROM nginx:stable-alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]