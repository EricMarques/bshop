from django.db import models

# Create your models here.


#  Service
class Service(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=30,
        blank=False,
        null=False,
    )

    description = models.TextField(
        verbose_name='Descrição',
        max_length=200,
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        verbose_name='Valor',
        max_digits=6,
        decimal_places=2,
    )

    status = models.BooleanField(
        verbose_name='Status',
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Alterado em',
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return f'{self.name}'


#  Address
class Address(models.Model):
    street = models.CharField(
        verbose_name='Rua',
        max_length=100,
        blank=True,
        null=True,
    )

    number = models.CharField(
        verbose_name='Número',
        max_length=8,
        blank=True,
        null=True,
    )

    complement = models.CharField(
        verbose_name='Complemento',
        max_length=100,
        blank=True,
        null=True,
    )

    neighborhood = models.CharField(
        verbose_name='Bairro',
        max_length=100,
        blank=True,
        null=True,
    )

    city = models.CharField(
        verbose_name='Cidade',
        max_length=100,
        blank=True,
        null=True,
    )

    state = models.CharField(
        verbose_name='Estado',
        max_length=30,
        blank=True,
        null=True,
    )

    country = models.CharField(
        verbose_name='País',
        max_length=50,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Alterado em',
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return 'Rua: {}, Nº: {}'.format(self.street, self.number)


#  Professional
class Professional(models.Model):
    GENDER_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    first_name = models.CharField(
        verbose_name='Nome',
        max_length=30,
        blank=False,
        null=False,
    )

    second_name = models.CharField(
        verbose_name='Sobrenome',
        max_length=100,
        blank=False,
        null=False,
    )

    birth_date = models.DateField(
        verbose_name='Data de nascimento',
        blank=True,
        null=True,
    )

    gender = models.CharField(
        verbose_name='Gênero',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=False,
        null=False,
    )

    service = models.ManyToManyField(
        Service,
        verbose_name='Serviço',
    )

    address = models.ForeignKey(
        Address,
        verbose_name='Endereço',
        related_name='professionals',
        on_delete=models.CASCADE,
        help_text='Endereço',
        null=False,
    )

    status = models.BooleanField(
        verbose_name='Status',
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Alterado em',
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    def full_name(self):
        return '{} {}'.format(self.first_name, self.second_name)

    def __str__(self):
        return self.first_name


#  Establishment
class Establishment(models.Model):
    name = models.CharField(
        verbose_name='Nome Fantasia',
        max_length=50,
        blank=True,
        null=True,
    )

    company_name = models.CharField(
        verbose_name='Razão Social',
        max_length=50,
        blank=True,
        null=True,
    )

    registered_number = models.CharField(
        verbose_name='CNPJ',
        max_length=100,
        blank=False,
        null=False,
    )

    municipal_registration = models.CharField(
        verbose_name='Inscrição Municipal',
        max_length=20,
        blank=True,
        null=True,
    )

    address = models.ForeignKey(
        Address,
        verbose_name='Endereço',
        related_name='establishment',
        on_delete=models.CASCADE,
        help_text='Endereço',
        null=False,
    )

    status = models.BooleanField(
        verbose_name='Status',
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Alterado em',
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
