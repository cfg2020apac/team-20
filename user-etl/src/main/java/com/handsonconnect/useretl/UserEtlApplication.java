package com.handsonconnect.useretl;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication
public class UserEtlApplication {

	public static void main(String[] args) {
		SpringApplication.run(UserEtlApplication.class, args);
	}

}
