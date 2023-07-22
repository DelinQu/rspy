python video_to_gif.py \
    --rsv=/home/qdl/Desktop/PJLAB/pj/QRST/RSC/videos/3GS_rs_seq.mp4 \
    --rscv=/home/qdl/Desktop/PJLAB/pj/QRST/RSC/videos/3GS_QRST_seq.mp4 \
    --gif=/home/qdl/Desktop/PJLAB/repo/rspy/assets/images/3gs.gif \
    --step=1 \
    --fps=10 \
    --rs_delay=2 \
    --start=50

# * GPark
# python video_crop.py \
#     --input=/home/qdl/Desktop/PJLAB/pj/QRST/RSC/videos/GPark_QRST_seq.mp4 \
#     --output=GPark_QRST_seq_cropped.mp4 \
#     --ratio=0.025

# python video_crop.py \
#     --input=/home/qdl/Desktop/PJLAB/pj/QRST/RSC/videos/GPark_rs_seq.mp4 \
#     --output=GPark_rs_seq_cropped.mp4 \
#     --ratio=0.025

python video_to_gif.py \
    --rsv=GPark_rs_seq_cropped.mp4 \
    --rscv=GPark_QRST_seq_cropped.mp4 \
    --gif=/home/qdl/Desktop/PJLAB/repo/rspy/assets/images/gpark.gif \
    --step=1 \
    --fps=0.5 \
    --rs_delay=2 \
    --start=25 \
    --end=-10
