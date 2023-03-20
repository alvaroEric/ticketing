from django.db import models

# declare a new model with a name "Tickets"
class Tickets(models.Model):
    ticket_id = models.CharField(max_length= 200)
    ticket_body = models.TextField()
    request_name = models.CharField(max_length= 200)
    request_subject = models.CharField(max_length= 200)
    ticket_date = models.DateTimeField(auto_now_add=True)

    # __str__method is define to return a name of instances of Tichet model 
    # which is ticket_id
    def __str__(self):
        return self.ticket_id

class ITTeam(models.Model):
    staff_id = models.CharField(max_length= 200)
    f_name = models.CharField(max_length= 200)
    l_name = models.CharField(max_length= 200)
    username = models.CharField(max_length= 200)
    
    #foreignkey from Tickets
    ticketNumber = models.ForeignKey(Tickets, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.f_name, self.l_name)

class TicketReport(models.Model):
    #foreignkey from Tickets
    ticketNumber = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    #foreignkey from ITTeam
    itsuppoter = models.ForeignKey(ITTeam, on_delete=models.CASCADE)
    

    

