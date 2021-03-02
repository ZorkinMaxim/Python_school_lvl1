plane_altitude         = 500    # meters
plane_speed            = 200    # km/hours
wind_speed             = 50     # km/hours
wind_direction         = "North"
plane_direction        = "South"
free_landing_line      = False

fuel_level             =  2    # %
emergency_landing_need = False


can_land = 100 <= plane_altitude < 700 and 200 <= plane_speed < 500 \
           and wind_speed < 100\
           and plane_direction != wind_direction\
           and free_landing_line == True

emergency_land = fuel_level <= 5 or emergency_landing_need == True

print("Can the plane land? ", can_land)
print("Can the plane land in an emergency?", emergency_land)
print()
print("plane_altitude =", plane_altitude, "\n" "plane_speed =", plane_speed, "\n" "wind_speed =", wind_speed, "\n"\
      "wind_direction =", wind_direction, "\n" "plane_direction =", plane_direction, "\n"\
      "free_landing_line =", free_landing_line, "\n" "fuel_level =", fuel_level, "\n"\
      "emergency_landing_need =", emergency_landing_need, "\n")