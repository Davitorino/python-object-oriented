from abc import ABC, abstractmethod


class Animal(ABC):
	@abstractmethod
	def __init__(self, tamanho_passo: int):
		self.__tamanho_passo = tamanho_passo

	@property
	def tamanho_passo(self):
		return self.__tamanho_passo

	@tamanho_passo.setter
	def tamanho_passo(self, tamanho_passo: int):
		self.__tamanho_passo = tamanho_passo

	def mover(self):
		return f'ANIMAL: DESLOCOU {self.__tamanho_passo}'

	@abstractmethod
	def produzir_som(self):
		return 'PRODUZ SOM:'
