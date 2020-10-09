package com.handsonconnect.useretl.controller;

import com.handsonconnect.useretl.model.NGO;
import com.handsonconnect.useretl.repository.NGORepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "${v1API}/ngo")
public class NGOController {

    @Autowired
    private NGORepository ngoRepository;

    //http://localhost:8083/api/v1/ngo/partners
    @PostMapping(value="/partners", consumes="application/json", produces="application/json")
    public ResponseEntity<NGO> newPartner(@RequestBody NGO ngo){
        NGO result = ngoRepository.save(ngo);
        return ResponseEntity.status(HttpStatus.CREATED).body(result);
    }

    //http://localhost:8083/api/v1/ngo/partners
    @GetMapping(value="/partners", produces="application/json")
    public ResponseEntity<List<NGO>> all(){
        List<NGO> results = ngoRepository.findAll();
        return ResponseEntity.status(HttpStatus.CREATED).body(results);
    }
}
