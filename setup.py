from setuptools import setup, find_packages
__version__ = '0.1.0-alpha.1'
setup(
    name='face_recognizer',
    version=__version__,
    description='Recognition implement with MTCNN and VGGFace',
    url='https://github.com/Uysim/face-recognizer',
    author='Uysim Ty',
    author_email="uysimty@gmail.com",
    license='MIT',
    keywords=['face detection', 'face match', 'mtcnn', 'tensorflow', 'keras', 'vggface', 'deeplearning'],
    packages=find_packages(exclude=["test", "image",".venv"]),
    zip_safe=False,
    install_requires=[
        'tensorflow<2.13.0', # https://github.com/rcmalli/keras-vggface/issues/97
        'mtcnn>=0.1.0',
        'keras_applications>=1.0.8',
        'keras_vggface @ git+https://github.com/rcmalli/keras-vggface.git',
    ],
    extras_require={
        "tf": ["tensorflow"],
        "tf_gpu": ["tensorflow-gpu"],
    }
)