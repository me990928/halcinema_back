from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from model.test import Test
from model.m_advertisements import Advertisement
from model.m_advertisement_types import AdvertisementType
from model.m_movies import Movie
from model.m_movie_genres import MovieGenre
from model.m_movie_titles import MovieTitle
from model.m_screens import Screen
from model.m_screen_types import ScreenType
from model.m_ticket_types import TicketType
from model.m_users import User
from model.t_appointments import Appointment
from model.t_appointment_details import AppointmentDetail
from model.t_general_inquiries import GeneralInquiry
from model.t_member_genres import MemberGenre
from model.t_payments import Payment
from model.t_seats import Seat
from model.t_theater_schedules import TheaterSchedule
from model.m_movie_pict import MoviePict

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [
    Test.metadata, 
    Advertisement.metadata, 
    AdvertisementType.metadata, 
    Movie.metadata,
    MovieGenre.metadata,
    MovieTitle.metadata,
    Screen.metadata,
    ScreenType.metadata,
    TicketType.metadata,
    User.metadata,
    Appointment.metadata,
    AppointmentDetail.metadata,
    GeneralInquiry.metadata,
    MemberGenre.metadata,
    Payment.metadata,
    Seat.metadata,
    TheaterSchedule.metadata,
    MoviePict.metadata
    ]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    url = config.get_main_option("sqlalchemy.url")

    with connectable.connect() as connection:
        context.configure(
            url = url,
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
