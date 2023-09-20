from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def send_otp(request):
    # data = request.data
    mobile_no = request.data.get('mobile_no')
    password = request.data.get('password')

    if mobile_no is None:
        return Response({
            'status': 400,
            'message': 'key mobile_no is required'
        })

    if password is None:
        return Response({
            'status': 400,
            'message': 'key password is required'
        })
    
    otp = send_otp_to_phone(mobile_no)
    if otp is None:
        return Response({
            'status': 400,
            'message': 'Failed to generate OTP'
        })


    user = User.objects.create(
        mobile_no = mobile_no,
        otp = otp
    )

    user.set_password = password
    user.save()

    return  Response({
        'status': 200,
        'message': "OTP sent"
    })


@csrf_exempt
@api_view(['POST'])
def resend_otp(request):
    # data = request.data
    mobile_no = request.data.get('mobile_no')

    if mobile_no is None:
        return Response({
            'status': 400,
            'message': 'key mobile_no is required'
        })
    
    try:
        user_obj = User.objects.get(mobile_no = mobile_no)
        otp = send_otp_to_phone(mobile_no)
        if otp is None:
            return Response({
                'status': 400,
                'message': 'Failed to generate OTP'
            })

        user_obj.otp = otp
        user_obj.save()

        return  Response({
            'status': 200,
            'message': "OTP sent"
        })

    except Exception as e:
        return Response({
            'status': 400,
            'message': 'Invalid mobile no.!'
        })


@csrf_exempt
@api_view(['POST'])
def verify_otp(request):
    # data = request.data
    mobile_no = request.data.get('mobile_no')
    otp = request.data.get('otp')

    if mobile_no is None:
        return Response({
            'status': 400,
            'message': 'key mobile_no is required'
        })

    if otp is None:
        return Response({
            'status': 400,
            'message': 'key otp is required'
        })


    try:
        user_obj = User.objects.get(mobile_no = mobile_no)
        if otp == user_obj.otp:
            user_obj.is_mobile_verified = True
            return  Response({
                'status': 200,
                'message': "OTP Verified!"
            })
        return  Response({
                'status': 400,
                'message': "Invalid OTP!"
            })

    except Exception as e:
        return Response({
            'status': 400,
            'message': 'Invalid mobile no.!'
        })