from setuptools import setup

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    url='http://github.com/rizkiarm/LipNet',
    author='Muhammad Rizki A.R.M',
    author_email='rizki@rizkiarm.com',
    license='MIT',
    packages=['lipnet'],
    zip_safe=False,
	install_requires=[
        'Keras==2.0.2',
        'editdistance==0.3.1',
		'h5py==2.6.0',
		'numpy==1.12.1',
		'python-dateutil==2.6.0',
		'Pillow==4.1.0',
		'Theano==0.9.0',
        'sk-video==1.1.7',
        'dlib==19.4.0'
    ])
