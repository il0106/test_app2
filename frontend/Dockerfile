FROM node:24.2

WORKDIR /app

COPY package*.json ./
RUN npm install -g npm@latest && npm install

COPY . .

RUN npm run build

CMD ["node", ".output/server/index.mjs"]