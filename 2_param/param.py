import click

class BasedINTParamType(click.ParamType):
    name = "integer"

    def convert(self, value, param, ctx):
        if isinstance(value,int):
            return value

        try:
            if value[:2].lower()=="0x":
                return int(value[2:],16)
            elif value[:1]=="0":
                return int(value,8)
            else:
                int(value,10)
        except ValueError:
            self.fail(f"{value} is not a valid integer",param,ctx)

BASED_INT=BasedINTParamType()