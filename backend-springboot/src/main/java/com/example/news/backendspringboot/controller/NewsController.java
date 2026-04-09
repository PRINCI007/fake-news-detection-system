package com.example.news.backendspringboot.controller;

import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/news")
@CrossOrigin(origins = "*")  // allows frontend access
public class NewsController {

    @PostMapping("/predict")
    public ResponseEntity<String> predictNews(@RequestBody Map<String, String> request) {

        String flaskUrl = "http://127.0.0.1:5000/predict";

        // Prepare request to Flask
        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, String>> entity = new HttpEntity<>(request, headers);

        // Call Flask API
        ResponseEntity<String> response = restTemplate.postForEntity(
                flaskUrl,
                entity,
                String.class
        );

        return ResponseEntity.ok(response.getBody());
    }
}