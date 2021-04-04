from django.db import models
# from ..products.models import Dish
# from ..company.models import Company

class BudgetHeader(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    zip_code = models.CharField(max_length=12)
    cpf = models.IntegerField()
    people_qtd = models.IntegerField()
    space_restriction = models.BooleanField()
    need_waiter = models.BooleanField()
    want_entrance = models.BooleanField()
    budget_date = models.DateField(auto_now_add=True)
    event_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    event_date = models.DateField()
    duration_hours = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'BudgetHeader'
        verbose_name_plural = u'BudgetsHeader'
        ordering = ['-event_date']
    

class BudgetItem(models.Model):
    dish = models.ForeignKey('products.Dish', on_delete=models.CASCADE)
    budget_header = models.ForeignKey(BudgetHeader, on_delete=models.CASCADE)
    qtd_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    cost_person_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    cost_distance_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    cost_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
            return self.dish

    class Meta: 
        verbose_name = u'BudgetItem'
        verbose_name_plural = u'BudgetItems'

    def save_budget_item(self, *args, **kwargs):
        self.qtd_total = self.dish.qnt_per_people * self.budget_header.people_qtd
        self.cost_distance_total = self.dish.cost_per_distance * self.budget_header.people_qtd
        self.cost_person_total = self.dish.cost_per_people * self.budget_header.event_distance
        self.cost_total = self.cost_person_total + self.cost_distance_total
        return super(BudgetItem, self).save(*args, **kwargs)
