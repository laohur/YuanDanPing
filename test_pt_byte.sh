model_name=$1
model_name_or_path=/mnt/cool/llm/ChuanyueTest/models/${model_name}
if [ ! -d $model_name_or_path ];then
    exit 
fi
output_dir=./outputs-byte/${model_name}
if [ -d $output_dir ];then
    exit 
fi
echo $model_name
echo $model_name_or_path
echo $output_dir
# exit
python pt.py \
    --model_type llama \
    --model_name_or_path $model_name_or_path \
    --tokenizer_name_or_path google/byt5-base \
    --train_file_dir /mnt/cool/dataset/wikinews/2023.jsonl \
    --validation_file_dir /mnt/cool/dataset/wikinews/2024-01.jsonl \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 2 \
    --do_train \
    --do_eval \
    --use_peft True \
    --seed 42 \
    --max_train_samples 100000 \
    --max_eval_samples 10000 \
    --num_train_epochs 1 \
    --learning_rate 2e-4 \
    --warmup_ratio 0.05 \
    --weight_decay 0.01 \
    --logging_strategy steps \
    --logging_steps 100 \
    --eval_steps 5000 \
    --evaluation_strategy steps \
    --save_steps 1000000 \
    --save_strategy steps \
    --save_total_limit 1 \
    --gradient_accumulation_steps 1 \
    --preprocessing_num_workers 2 \
    --block_size 1024 \
    --group_by_length True \
    --output_dir $output_dir \
    --overwrite_output_dir \
    --ddp_timeout 30000 \
    --logging_first_step True \
    --target_modules all \
    --modules_to_save "embed_tokens,lm_head,norm" \
    --lora_rank 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --torch_dtype bfloat16 \
    --bf16 \
    --device_map auto \
    --report_to tensorboard \
    --ddp_find_unused_parameters False \
    --gradient_checkpointing True \
    --cache_dir ./cache 

