from rest_framework import serializers
from application.models import Address, Applicant

class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Address
        fields = ('__all__')

class ApplicantSerializer(serializers.ModelSerializer):
    address = AddressSerializer(
        many=True
    )
    class Meta:
        model = Applicant
        fields = ('id','first_name','last_name','income','address')

    def create(self, validated_data):
        address_list = validated_data.pop('address')
        applicant = Applicant.objects.create(**validated_data)
        for address_data in address_list:
            address = Address.objects.get(pk=address_data.get('id'))
            applicant.address.add(address)
        return applicant

    def update(self, instance, validated_data):
        address_list = validated_data.pop('address')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.income = validated_data.get('income', instance.income)
        instance.address = []
        for address_data in address_list:
            address = Address.objects.get(pk=address_data.get('id'))
            instance.address.add(address)
        instance.save()
        return instance
