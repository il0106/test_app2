FROM node:24.2

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install -g npm@latest && npm install

# COPY . .
COPY ./.env ./.env
COPY ./frontend .


RUN npm run build

CMD ["node", ".output/server/index.mjs"]