# Vs (top_p & temperature)

| Example use case      | temperature | top_p | Description                                                                                                                                                      |
|-----------------------|-------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Brainstorming session | High        | High  | High randomness with large pool of potential tokens. The results will be highly diverse, often leading to very creative and unexpected results.                  |
| Email generation      | Low         | Low   | Deterministic output with high probable predicted tokens. This results in predictable, focused, and conservative outputs.                                        |
| Creative writing      | High        | Low   | High randomness with a small pool of potential tokens. This combination produces creative outputs but still remains coherent.                                    |
| Translation           | Low         | High  | Deterministic output with high probable predicted tokens. Produces coherent output with a wider range of vocabulary, leading to outputs with linguistic variety. |
