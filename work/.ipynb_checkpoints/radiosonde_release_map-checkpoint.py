import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# Define two points in the Arabian Sea region as (longitude, latitude)
point1 = (60.0, 20.0)  # Near the coast of Oman
point2 = (70.0, 15.0)  # Central Arabian Sea

# Create a figure and axis with Plate Carree projection
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Set the extent to focus on the Arabian Sea region
ax.set_extent([40, 80, 5, 30], crs=ccrs.PlateCarree())

# Add map features
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.STATES, linestyle=':')
ax.gridlines(draw_labels=True)

# Plot the two points
ax.plot(point1[0], point1[1], 'ro', markersize=8, transform=ccrs.PlateCarree(), label='Point 1')
ax.plot(point2[0], point2[1], 'bo', markersize=8, transform=ccrs.PlateCarree(), label='Point 2')

# Add a legend and title
ax.legend()
plt.title('Map of Arabian Sea Region with Two Points')

plt.show()