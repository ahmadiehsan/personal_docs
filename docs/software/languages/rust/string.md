# String

## Variances

```rust
let hello: String = String::from("नमस्ते");

// Bytes
// [224, 164, 168, 224, 164, 174, 224, 164, 184, 224, 165, 141, 224, 164, 164, 224, 165, 135]

// Scalar values
// ['न', 'म', 'स्', 'त', 'े']

// Grapheme clusters
// ["न", "म", "स्", "ते"]
```

## Loop

- Bytes

  ```rust
  for b: u8 in "नमस्ते".bytes() {
      println!("{}", b);
  }
  ```

- Scalar

  ```rust
  for c: char in "नमस्ते".chars() {
      println!("{}", c);
  }
  ```

- Grapheme

  ```rust
  for g: &str in "नमस्ते".graphemes(is_extended: true) {
      println!("{}", g);
  }
  ```
