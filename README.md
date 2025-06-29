# Geração de Imagens com Stable Diffusion XL

Este projeto é uma demonstração de como utilizar o modelo Stable Diffusion XL (SDXL) para gerar imagens a partir de descrições textuais (prompts). A Stable Diffusion é uma das mais avançadas redes neurais de difusão text-to-image, capaz de criar imagens de alta qualidade e complexidade a partir de linguagem natural.

## Visão Geral

A Geração de Imagens Text-to-Image transformou a maneira como criamos conteúdo visual. A Stable Diffusion XL, em particular, é um modelo de ponta que oferece:
* **Qualidade de Imagem Superior:** Gera imagens mais detalhadas e fotorrealistas.
* **Melhor Compreensão de Prompts:** Interpreta melhor as descrições complexas e abstratas.
* **Geração Versátil:** Produz uma ampla gama de estilos artísticos e tipos de conteúdo.

Este notebook configura um ambiente para carregar o modelo SDXL e gerar uma imagem baseada em um `prompt` e um `negative_prompt` (prompt negativo, para especificar o que *não* queremos na imagem).

## Estrutura do Projeto

* `stablediffusion.py`: O arquivo que contém todo o código para configurar o ambiente, carregar o modelo SDXL e gerar imagens.

## Tecnologias Utilizadas

* **Python 3**
* **Hugging Face `diffusers` library**: Para acesso e utilização facilitada do modelo Stable Diffusion XL.
* **`torch` (PyTorch)**: Como backend para as operações de tensor, aproveitando a aceleração por GPU.
* **Matplotlib**: Para exibir a imagem gerada.
* **`hf_xet`**: Uma dependência para lidar com grandes arquivos de modelos do Hugging Face.


## Parâmetros de Geração

Você pode ajustar os seguintes parâmetros no notebook para controlar a imagem gerada:

* `pretrained_model`: O nome do modelo pré-treinado (e.g., `"stabilityai/stable-diffusion-xl-base-1.0"`).
* `prompt`: A descrição textual da imagem que você deseja gerar. Seja criativo e específico!
* `negative_prompt`: Uma descrição do que você *não* quer na imagem, para guiar o modelo.
* `num_inference_steps`: O número de etapas de difusão. Mais etapas geralmente resultam em mais detalhes, mas demoram mais.
* `guidance_scale`: (ou `cfg_scale`) A intensidade com que o modelo segue o prompt. Valores mais altos (e.g., 7-10) resultam em imagens mais próximas do prompt.
* `height`, `width`: Dimensões da imagem de saída em pixels.
* `seed`: Um valor numérico para reproduzir os mesmos resultados de geração (para uma semente fixa, o mesmo prompt e parâmetros produzirão a mesma imagem).

## Exemplo de Saída

Prompt usado para gerar a imagem abaixo: "Sketch drawing of a 90s Formula 1 car"

![Image](https://github.com/user-attachments/assets/9bcddbaf-9526-4ae7-a210-9d15fbb60761)
