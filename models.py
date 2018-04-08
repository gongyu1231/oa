from django.db import models

class S20ticket(models.Model):
    no = models.CharField('后台订单号', max_length = 20, blank = True, null = True)
    name = models.CharField('姓名', max_length = 20, blank=True,null=True)
    mobile = models.CharField('手机号码', max_length = 20, blank=True,null=True)
    kol = models.CharField('KOL', max_length = 20, blank=True,null=True)
    t_list = (
	(1, 'GA13日'),
        (2, 'GA14日'),
        (3, 'GA15日'),
        (4, 'GA3天通票'),
        (5, 'VIP3天通票'),
    )
    title = models.IntegerField('票类型', choices=t_list)
    quantity = models.CharField('数量', max_length = 20, default = 1)
    money = models.BigIntegerField('实际收费')
    add = models.CharField('邮寄地址', max_length = 120, blank=True,null=True)
    money_sts = (
        (1,'已付款'),
        (2,'仅口嗨'),
        (3,'已邮寄'),
        (4,'已收到'),
        (5,'已取消'),
    )
    msts = models.IntegerField('付款状态', choices=money_sts, default = 1)
    reason = models.CharField('备注', max_length = 120, blank=True,null=True)
    timestamp = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return str(self.name)

class S20hotel(models.Model):
    no = models.CharField('后台订单号', max_length = 20, blank=True,null=True)
    name = models.CharField('姓名', max_length = 20,null=True)
    ename = models.CharField('英文姓名', max_length = 20,null=True)
    passport = models.CharField('护照号码', max_length = 20,null=True)
    name2 = models.CharField('姓名2', max_length = 20, blank=True,null=True)
    ename2 = models.CharField('英文姓名2', max_length = 20,blank=True,null=True)
    passport2 = models.CharField('护照号码2', max_length = 20,blank=True,null=True)
    mobile = models.CharField('手机号码', max_length = 20, null = True)
    kol = models.CharField('KOL', max_length = 20,)
    t_list = (
	(1, '大床'),
        (2, '双床'),
        (3, '套房'),
        (4, '别墅'),
    )
    title = models.IntegerField('房间类型', default = 1, choices=t_list)
    money = models.BigIntegerField('实际收费')
    money_sts = (
        (1,'已付款'),
        (2,'仅口嗨'),
        (3,'已取消'),
    )
    msts = models.IntegerField('付款状态', choices=money_sts, default = 1)
    reason = models.CharField('备注', max_length = 120, blank=True,null=True)
    timestamp = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return str(self.name)