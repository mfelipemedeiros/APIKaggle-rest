package com.aps.APIKaggle.dtos;

import com.aps.APIKaggle.security.RoleName;

public record CreateUserDto(

        String email,
        String password,
        RoleName role

) {
}