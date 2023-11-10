package com.aps.APIKaggle.controllers;

import com.aps.APIKaggle.models.ProductModel;
import com.aps.APIKaggle.repositories.ProductRepository;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/kaggle/v1")
public class ProductController {
    @Autowired
    ProductRepository productRepository;

    @PostMapping("/products/add")
    public ResponseEntity<ProductModel> save(@RequestBody ProductModel product) {
        ProductModel shoes = productRepository.save(product);
        return ResponseEntity.status(HttpStatus.CREATED).body(productRepository.save(shoes));
    }

    @GetMapping("/products")
    public ResponseEntity<List<ProductModel>> getAll() {
        List<ProductModel> shoes = productRepository.findAll();

        return ResponseEntity.status(HttpStatus.OK).body(shoes);
    }

    @GetMapping("/get/{id}")
    public ResponseEntity<Object> getOneProduct(@PathVariable(value = "id") Long id) {
        Optional<ProductModel> shoes = productRepository.findById(id);
        if(shoes.isEmpty()){
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Produto Não encontrado");
        }
        return ResponseEntity.ok(shoes);
    }
    @PutMapping("/products/alterFull/{id}")
    public ResponseEntity<Object> changeAll(@PathVariable(value = "id") Long id, @RequestBody ProductModel product){
        Optional<ProductModel> shoes = productRepository.findById(id);
        if(shoes.isEmpty()){
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Produto Não encontrado");
        }

        var shoesNew = shoes.get();
        return  ResponseEntity.status(HttpStatus.OK).body(productRepository.save(shoesNew));
    }
    @PatchMapping("/products/alter/{id}")
    public ResponseEntity<Object> change(@PathVariable(value = "id") Long id, @RequestBody ProductModel product){
        Optional<ProductModel> shoes = productRepository.findById(id);
        if(shoes.isEmpty()){
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Produto Não encontrado");
        }
        var shoesNew = shoes.get();
        return  ResponseEntity.status(HttpStatus.OK).body(productRepository.save(shoesNew));
    }
    @DeleteMapping("/products/delete/{id}")
    public ResponseEntity<Object> delete(@PathVariable(value = "id") Long id){
        Optional<ProductModel> shoes = productRepository.findById(id);
        if(shoes.isEmpty()){
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Produto Não encontrado");
        }
        productRepository.delete(shoes.get());
        return ResponseEntity.status(HttpStatus.OK).body("Product deleted succesfully.");
    }
}
