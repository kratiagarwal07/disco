import os, time

cmd1 = "IMAGE_SIZE=224"
cmd2 = 'ARCHITECTURE="mobilenet_1.0_${IMAGE_SIZE}"'
cmd3 = "tensorboard --logdir files/training_summaries &"
cmd4 = 'python -m scripts.retrain --bottleneck_dir=files/bottlenecks --how_many_training_steps=1000 --model_dir=files/models/ --summaries_dir=files/training_summaries/"${ARCHITECTURE}" --output_graph=files/retrained_graph.pb --output_labels=files/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=files/images'

after = "&&"

os.system(cmd3)
os.system(cmd1 + after + cmd2 + after + cmd4)

time.sleep(10)
os.system('kill `ps -ax | grep "tensorboard"`')
