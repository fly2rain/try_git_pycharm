import sys
sys.path.append("/Users/f0z00qt/fyzhu_all/pycharm/IRAS-Keyword-Feature-Vector-Classifier-Auto-Training_fz")
print("print sys.path ...")
for x in sys.path:
    print(x)

if __name__ == "__main__":
    from run_google_ocr import GetGoogleOCRImagewise

    GetGoogleOCRImagewise.get_image_list("")


