# Changelog


## [5.12.0]

### Updated

- The `sqlalchemy` dependency has been updated to `1.4` because we are using [overlaps](https://docs.sqlalchemy.org/en/20/orm/relationship_api.html#sqlalchemy.orm.relationship.params.overlaps) in the `Gnotification` class.


## [5.2.4]

### Updated

- Updated the `User` class to include the `uuid`.
- Updated the `Gnotifications` class to include the `uuid`.

## [5.2.0]

### Added

- Created the following tables:
  - `Gnotification`
  - `GnotificationCcEmail`
  - `GnotificationContainerFieldAsc`
  - `UserRole`
  - `UserUserRoleAsc`
  - `Customer`
  - `CustomerUserAsc`

### Updated

- Updated the `User` class to include the following relationships:
  - `gnotifications`
  - `user_roles`
  - `customers`
- Updated the `ContainerField` class to include the `gnotifications` relationship.
- Updated the `workflow/release.yml` file to include a test release step.
