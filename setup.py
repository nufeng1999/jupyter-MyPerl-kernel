from setuptools import setup

setup(name='jupyter_MyPerl_kernel',
      version='0.0.1',
      description='Minimalistic Perl kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyPerl-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyPerl-kernel/tarball/0.0.1',
      packages=['jupyter_MyPerl_kernel'],
      scripts=['jupyter_MyPerl_kernel/install_MyPerl_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'Perl','pl'],
      include_package_data=True
      )
