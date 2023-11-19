package com.aps.APIKaggle.models;

import jakarta.persistence.*;
import org.springframework.hateoas.RepresentationModel;

import java.io.Serializable;
import java.util.Objects;

@Entity
@Table(name = "APIAPS")
public class ProductModel extends RepresentationModel<ProductModel> implements Serializable {

    @Id
    @TableGenerator(name = "sua_entidade_gen", table = "id_generator",
            pkColumnName = "gen_name", valueColumnName = "gen_value",
            initialValue = 3269, allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.TABLE, generator = "sua_entidade_gen")
    @Column(name = "id")
    private Long id;
    @Column(name = "product_name", length = 200)
    private String product_name;
    @Column(name = "product_id", length = 25)
    private String product_id;
    @Column( name = "listing_price", length = 6)
    private int listing_price;
    @Column (name = "sale_price", length = 6)
    private int sale_price;
    @Column (name = "discount", length = 3)
    private int discount;
    @Column( name = "brand", length = 100)
    private String brand;
    @Column(name = "rating",length = 3)
    private float rating;
    @Column( name = "reviews",length = 4)
    private int reviews;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getProduct_name() {
        return product_name;
    }

    public void setProduct_name(String product_name) {
        this.product_name = product_name;
    }

    public String getProduct_id() {
        return product_id;
    }

    public void setProduct_id(String product_id) {
        this.product_id = product_id;
    }

    public int getListing_price() {
        return listing_price;
    }

    public void setListing_price(int listing_price) {
        this.listing_price = listing_price;
    }

    public int getSale_price() {
        return sale_price;
    }

    public void setSale_price(int sale_price) {
        this.sale_price = sale_price;
    }

    public int getDiscount() {
        return discount;
    }

    public void setDiscount(int discount) {
        this.discount = discount;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public float getRating() {
        return rating;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }

    public int getReviews() {
        return reviews;
    }

    public void setReviews(int reviews) {
        this.reviews = reviews;
    }

    @Override
    public String toString() {
        return "ProductModel{" +
                "id=" + id +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        ProductModel that = (ProductModel) o;
        return Objects.equals(id, that.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), id);
    }
}
