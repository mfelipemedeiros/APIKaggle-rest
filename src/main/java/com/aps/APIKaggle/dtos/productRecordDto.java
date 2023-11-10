package com.aps.APIKaggle.dtos;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

import java.math.BigDecimal;

public record productRecordDto(@NotBlank String name, @NotNull BigDecimal value) {
}
