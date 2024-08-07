from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey,  Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("hashed_password", String),
    Column("email", String),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


color = Table(
    "color",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("color", String),
)

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("price", Integer),
    Column("color_id", Integer),
    Column("ret", Integer),
)
