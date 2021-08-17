from regression_model.config.core import config
from regression_model.processing.features import(
    EngineVariableTransformer,
    ManifactureVariableTransformer,
    Mapper
)


def test_engine_variable_transformer(sample_input_data):
    # Given
    transformer = EngineVariableTransformer(
        variables=[config.model_config.engine_vars]
    )
    assert sample_input_data["Engine"].iat[0] == '1248 CC'

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["Engine_ext"].iat[0] == 1248.0


def test_manifacture_variable_transformer(sample_input_data):
    # Given
    transformer = ManifactureVariableTransformer(
        variables=[config.model_config.name_vars]
    )
    assert sample_input_data["Name"].iat[0] == 'MARUTI VITARA BREZZA ZDI PLUS'

    # # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["Manifacture"].iat[0] == 'MARUTI'


def test_mapper(sample_input_data):
    # Given
    transformer = Mapper(
        variables=[config.model_config.owner_type_vars],
        mappings=config.model_config.owner_mappings
    )
    assert sample_input_data["Owner_Type"].iat[0] == 'First'

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["Owner_Type"].iat[0] == 1