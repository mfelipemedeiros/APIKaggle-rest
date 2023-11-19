package com.aps.APIKaggle.dtos;

import jakarta.persistence.Column;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

import java.math.BigDecimal;

public record productRecordDto(
        String product_name,
       String product_id,
       int sale_price,
       int discount,
       String brand, float rating,int reviews) {
}
