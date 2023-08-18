from drf_yasg import openapi

class ConfigSwagger():

    def __init__(self, header_param) -> None:
        header_param = openapi.Parameter(
            name="Authorization",
            in_= openapi.IN_HEADER,
            type = openapi.TYPE_STRING,
        ) 

        self.header_param = header_param


    @classmethod
    def errors_number(self, number, description):
        error_response = openapi.Response(
            description=f"Error: Unauthorized - { number }",
            schema=openapi.Schema(
                type='object',
                properties={
                    'detail': openapi.Schema(type='string', description=f"{ description }"),
                }
            ),
        )
        return error_response
    
    @classmethod
    def success_number(self, number, description):
        error_response = openapi.Response(
            description=f"Success: { number }",
            schema=openapi.Schema(
                type='object',
                properties={
                    'detail': openapi.Schema(type='string', description=f"{ description }"),
                }
            ),
        )
        return error_response