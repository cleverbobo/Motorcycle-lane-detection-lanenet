import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", help="Dataset path", default="./train_set1/training")
    parser.add_argument("--save", required=False, help="Directory to save model checkpoint", default="./checkpoints")
    parser.add_argument("--epochs", required=False, type=int, help="Training epochs", default=2000)
    parser.add_argument("--bs", required=False, type=int, help="Batch size", default=10)
    parser.add_argument("--val", required=False, type=bool, help="Use validation", default=False)
    parser.add_argument("--lr", required=False, type=float, help="Learning rate", default=0.0005)
    parser.add_argument("--pretrained", required=False, default=None, help="pretrained model path")
    parser.add_argument("--image", default="./output", help="output image folder")
    return parser.parse_args()
