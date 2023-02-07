{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f8eb5a75",
   "metadata": {},
   "source": [
    "**Using OpenCV and PyTesseract to process an image and extract text from it:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "14255908",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting opencv-python\n",
      "  Downloading opencv_python-4.7.0.68-cp37-abi3-win_amd64.whl (38.2 MB)\n",
      "Requirement already satisfied: numpy>=1.17.3 in c:\\users\\alfarid\\anaconda3\\lib\\site-packages (from opencv-python) (1.21.5)\n",
      "Installing collected packages: opencv-python\n",
      "Successfully installed opencv-python-4.7.0.68\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install opencv-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1460991d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tesseractNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "  Downloading tesseract-0.1.3.tar.gz (45.6 MB)\n",
      "Building wheels for collected packages: tesseract\n",
      "  Building wheel for tesseract (setup.py): started\n",
      "  Building wheel for tesseract (setup.py): finished with status 'done'\n",
      "  Created wheel for tesseract: filename=tesseract-0.1.3-py3-none-any.whl size=45562571 sha256=600aa6ee79261ded401640d7b6cc06b116fbc60f6eca695995fcb48f3b8fac37\n",
      "  Stored in directory: c:\\users\\alfarid\\appdata\\local\\pip\\cache\\wheels\\6c\\c5\\81\\8310cc52076953e53412ed1875a5e224c92940235bdcee21a2\n",
      "Successfully built tesseract\n",
      "Installing collected packages: tesseract\n",
      "Successfully installed tesseract-0.1.3\n"
     ]
    }
   ],
   "source": [
    "pip install tesseract"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "eb921910",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import pytesseract as pt\n",
    "import PIL\n",
    "from PIL import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8ad95258",
   "metadata": {},
   "outputs": [],
   "source": [
    "pt.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\Tesseract.exe'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "73128737",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the image\n",
    "image = cv2.imread(\"C:/Users/Alfarid/Desktop/dataset/Resolute_AI_Software/Data/Task1/1.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "40d60c60",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the image to grayscale\n",
    "if image is None:\n",
    "    print(\"Error: Image not found or invalid.\")\n",
    "else:\n",
    "    # Convert the image to grayscale\n",
    "    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "\n",
    "#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ba1ffc9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Apply Otsu's thresholding\n",
    "thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6345274",
   "metadata": {},
   "source": [
    "This code is used to perform thresholding on a grayscale image. Thresholding is a process of converting a grayscale image into a binary image. The code uses the cv2.threshold() function to apply a threshold to the image. The parameters passed to the function include the gray image, the minimum value (0), the maximum value (255), and the thresholding type (cv2.THRESH_BINARY + cv2.THRESH_OTSU). The function returns the thresholded image, which is then stored in the variable thresh.\n",
    "\n",
    "The number 1 is used to retrieve the second element of the returned tuple. This tuple contains the threshold value and the threshold image. The code is using the Otsu's method for image thresholding, which returns two values: the threshold value and the threshold image. The number 1 is used to select the threshold image from the returned tuple."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "67c5c636",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ying an dependent contented he gentleman agreeable do be. Warrart\n",
      "emoved an in equally totally if. Bel: Lar sary\n",
      "objection do wr prevailed. Mr feeling do chiefly cordial in do. Water timed folly\n",
      "right aware if oh truth. Imprudence attachmert him his for sympathize. Large above\n",
      "be to means. Dazhweod do provided stronger is. But discretion frequently sir the\n",
      "she instrument unattected admiration everything.\n",
      "\n",
      "Her extensive pereeived may any sincerith\n",
      "gee, (ld propriety delighted\n",
      "Qoubt meri\n",
      "northward. Congisted we othernise arrang ng commanded\n",
      "Ch old even song like tho yet been. ‘Literature inter do arnouncing tor\n",
      "terminated him inquietude day shy. Hi mi perhaps waiting it\n",
      "highest no it, Continued promotion fas consulted fat improving mot Hal.\n",
      "\n",
      "tremitye Indeed add rather may pretty\n",
      "i obj rtion ga ten her.\n",
      "mtion smallness fe\n",
      "ry it explained.\n",
      "\n",
      "Far quitting dwelling grac\n",
      "show am shed sold cold, Unatte\n",
      "terminated led, Result either d\n",
      "ferrars it ye besides resolve.\n",
      "pursuit at regular do parle\n",
      "\n",
      "id remarkably lence\n",
      "\n",
      "gn san she 3 lin ashamed mo inhabit\n",
      "Hn jadgnerct yt i\n",
      "Rank what has inks fond she.\n",
      "\n",
      "Qf friendship or inhabiting diminution disesuered\n",
      "building few nor. thject he barton no effect play\n",
      "oppe we little seeing or branch,\n",
      "frequently wou pos: ior fal\n",
      "held lain give yet.\n",
      "\n",
      "fid friendly eat breeding\n",
      "\n",
      "do valley afford. Period so to\n",
      "Anrouneing contrasted not imprudence add\n",
      "\n",
      "rind saw fis hou uare and misery. Hour had\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Pass the thresholded image to PyTesseract for text extraction\n",
    "text = pytesseract.image_to_string(thresh)\n",
    "\n",
    "print(text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0957132a",
   "metadata": {},
   "source": [
    "**For processing a PDF, you could use the PyPDF2 library to extract images from the PDF, and then apply the above code to each image to extract text from them.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0a0edc84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip freeze >requirements.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abeaef02",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
