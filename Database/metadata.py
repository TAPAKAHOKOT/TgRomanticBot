from sqlalchemy import MetaData

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix_%(table_name)s_%(all_column_names)s',
    'uq': 'uq_%(table_name)s_%(all_column_names)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': (
        'fk_%(table_name)s_%(all_column_names)s_%(referred_table_name)s'
    ),
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=convention)
