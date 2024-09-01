package com.openclassrooms.helloworld.model;

public class HelloWorld {

    private String message;

    // Constructeur par défaut
    public HelloWorld() {
        this.message = "Default Hello World Message";
    }

    // Constructeur avec message
    public HelloWorld(String message) {
        this.message = message;
    }

    // Getter pour message
    public String getMessage() {
        return message;
    }

    @Override
    public String toString() {
        return "Hello World !";
    }
}