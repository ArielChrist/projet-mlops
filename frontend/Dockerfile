FROM node:16-alpine AS build

WORKDIR /frontend


COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build


FROM nginx:1.23-alpine

COPY --from=build /frontend/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]