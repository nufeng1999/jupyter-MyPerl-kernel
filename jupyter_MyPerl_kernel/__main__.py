from ipykernel.kernelapp import IPKernelApp
from .kernel import MyPerlKernel
IPKernelApp.launch_instance(kernel_class=MyPerlKernel)
