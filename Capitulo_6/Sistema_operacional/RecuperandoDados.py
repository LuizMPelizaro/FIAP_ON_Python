import platform

print(f'Distibuição do Sistema Operacional.:{platform.platform()}\n'
      f'Nome do Sistema Operacional........:{platform.system()}\n'
      f'Versão do Sistema Operacional......:{platform.release()}\n'
      f'Arquitetura........................:{platform.architecture()}\n'
      f'Nome do computador.................:{platform.node()}\n'
      f'Tipo de Máquina....................:{platform.machine()}\n'
      f'Processador........................:{platform.processor()}\n'
      f'Versão do python...................:{platform.python_version()}')
