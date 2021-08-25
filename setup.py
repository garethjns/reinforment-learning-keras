import setuptools

from rlk import __version__

setuptools.setup(
    name="rlk",
    version=__version__,
    author="Gareth Jones",
    author_email="garethgithub@gmail.com",
    description="",
    long_description='',
    long_description_content_type="text/markdown",
    url="https://github.com/garethjns/reinforcement-learning-keras",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"],
    python_requires='>=3.6',
    install_requires=["tensorflow==2.5.1", "scikit-learn==0.23.0", "matplotlib", "gym[atari]==0.17.1",
                      "dataclasses", "tqdm", "seaborn", "joblib", "numpy", "coverage", "mock", "opencv-python",
                      "joblib", "tf2-vgpu"])
