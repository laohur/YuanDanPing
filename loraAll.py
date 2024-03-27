import os
from loguru import logger

corpus = "wikinews"
corpus = "UN_meeting_records"
corpus = "chinaxiv"


def eval(model_name, month, output_folder):
    model_path = f"{model_folder}/{model_name}"
    output_dir = f"{output_folder}/{model_name}"
    tgt = f"{output_dir}/eval_results.json"
    for model_type in ["auto", "AutoModel", "!"][:1]:
        for checkpointing in ["auto", "False", "True"][:1]:
            for use_fast_tokenizer in ["True", "False"]:
                if os.path.exists(tgt):
                    logger.info(f"{tgt} exists!")
                    return
                else:
                    logger.warning(f"{tgt} not exists!")
                    # return
                cmd = f"""
            CUDA_VISIBLE_DEVICES=0 python train.py \
                --model_type {model_type} \
                --model_name_or_path {model_path} \
                --tokenizer_name_or_path {model_path} \
                --use_fast_tokenizer {use_fast_tokenizer} \
                --train_file_dir ./input/{corpus}/2023.jsonl \
                --validation_file_dir ./input/{corpus}/{month}.jsonl \
                --per_device_train_batch_size 1 \
                --per_device_eval_batch_size 1 \
                --do_train  \
                --do_eval \
                --use_peft True \
                --seed 42 \
                --max_train_samples 10000 \
                --max_eval_samples 1000 \
                --num_train_epochs 1 \
                --learning_rate 2e-4 \
                --warmup_ratio 0.05 \
                --weight_decay 0.01 \
                --logging_strategy steps \
                --logging_steps 100 \
                --eval_steps 10000 \
                --evaluation_strategy steps \
                --save_steps 1000000 \
                --save_strategy steps \
                --save_total_limit 1 \
                --gradient_accumulation_steps 1 \
                --preprocessing_num_workers 2 \
                --block_size 1024 \
                --group_by_length True \
                --output_dir {output_dir} \
                --overwrite_output_dir \
                --ddp_timeout 30000 \
                --logging_first_step True \
                --target_modules all \
                --lora_rank 8 \
                --lora_alpha 16 \
                --lora_dropout 0.05 \
                --torch_dtype bfloat16 \
                --bf16 \
                --device_map auto \
                --report_to tensorboard \
                --ddp_find_unused_parameters False \
                --checkpointing {checkpointing} \
                --cache_dir ./cache     
                """
                logger.info(cmd)
                os.system(cmd)


model_folder = "/mnt/cool/models/foundation"
names = sorted(os.listdir(model_folder))


print(names)

# months = ["2024-01", "2024-02"][:]
months = ["2024"]
for month in months:
    output_folder = f"./output/{corpus}/outputs-lora/{month}"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for name in names:
        output_dir = f"{output_folder}/{name}"
        eval(name, month, output_folder)
