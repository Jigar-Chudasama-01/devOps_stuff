FROM openjdk:17-jdk-alpine

WORKDIR /app

COPY code.java /app/code.java

RUN javac code.java

CMD ["java", "code"]
