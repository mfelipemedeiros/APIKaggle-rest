package com.aps.APIKaggle.dtos;

import com.aps.APIKaggle.security.Role;

import java.util.List;

public record RecoveryUserDto(

        Long id,
        String email,
        List<Role> roles

) {
}
