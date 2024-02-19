# YueDanPing
reliable evalution for LLM foundation models monthly.


## result
perplexity: lower is better

| Foundation Models                          | just eval | train only lora | train with byt5 tokenizer |   |
|--------------------------------------------|-----------|-----------------|---------------------------|---|
| deepseek-llm-7b-base                       | 4.418595  | 2.775576        | 2.435999                  |   |
| Llama-2-7b-hf                              | 4.496019  | 2.775896        | 2.756618                  |   |
| Yi-6B                                      | 5.031991  | 2.996905        | 2.367179                  |   |
| CodeLlama-7b-hf                            | 5.087177  | 3.045621        | 2.888906                  |   |
| deepseek-coder-6.7b-base                   | 5.15121   | 3.079392        | 2.519493                  |   |
| llama-7b                                   | 5.287015  | 3.155645        | 2.37461                   |   |
| TinyLlama-1.1B-intermediate-step-240k-503b | 8.20445   | 4.419586        | 2.628365                  |   |