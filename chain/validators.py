from rest_framework.serializers import ValidationError

from chain.models import ChainUnit


def hierarchy_level_validator(data):
    """Ограничивает возможность выбора поставщика в зависимости от уровня иерархии текущего объекта сети"""
    print(data)
    if data.get('hierarchy_level') == 'factory' and data.get('supplier') != None:
        raise ValidationError('Ваш уровень иерархии - Завод. Это верхний уровень, вы не можете указать поставщика')
    elif data.get('hierarchy_level') == 'retail_chain' and data.get('supplier') != None:
        sup = ChainUnit.objects.get(id=data.get('supplier').id)
        if sup.hierarchy_level != 'factory':
            raise ValidationError('Ваш уровень иерархии - Розничная сеть. Вы можете выбрать только '
                                  'Завод в качестве поставщика')
    elif data.get('hierarchy_level') == 'retail_chain' or data.get('hierarchy_level') == 'ie' and data.get('supplier') == None:
        raise ValidationError('Требуется указать поставщика')
    elif data.get('hierarchy_level') == 'ie' and data.get('supplier') != None:
        sup = ChainUnit.objects.get(id=data.get('supplier').id)
        if sup.hierarchy_level != 'retail_chain':
            raise ValidationError('Ваш уровень иерархии - Индивидуальный преприниматель. Вы можете выбрать только '
                              'Розничную сеть в качестве поставщика')
